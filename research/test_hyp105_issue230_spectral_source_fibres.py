"""EICE-003-H exact W32/W34 true ORIGINAL GQ spectral fibre falsifiers."""
from collections import Counter
from fractions import Fraction
from itertools import combinations
import unittest

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_projection import fixture
from hyp105_issue230_spectral_source_fibres import (
    exact_incidence_spectral_polynomial, exact_middle_double_star_fibre,
    source_forest_signature, necessary_heavy_middle_five_source,
    finite_fibre_and_family_report, report,
)
from hyp105_issue230_five_source_blocked_search import (
    FiveSourceSearch, conditional_all_h_distinct_five_source_lower
)


class OriginalSpectralFibresTests(unittest.TestCase):
    def test_H1_TRUE_W32_W34_integer_GQ_incidence_polynomial(self):
        for power,scheme in ((1,'lex'),(2,'lex'),(2,'random')):
            with self.subTest(power=power,scheme=scheme):
                ctx=EndpointEnergy(fixture(power,scheme))
                cert=exact_incidence_spectral_polynomial(ctx)
                self.assertEqual(cert['all_V_squared_entries_checked'],ctx.v**2)
                self.assertEqual(cert['trivial_incidence_singular_value'],ctx.s+1)
                self.assertEqual(cert['nontrivial_incidence_singular_value_squared'],2*ctx.s)

    def test_H2_ALL_true_middle_source_fibres_and_independent_pencil_count(self):
        for power,scheme in ((1,'lex'),(1,'reverse'),
                             (1,'S68'),(1,'S72'),
                             (2,'lex'),(2,'random')):
            with self.subTest(power=power,scheme=scheme):
                ctx=EndpointEnergy(fixture(power,scheme))
                all_rows=[]
                for e in range(ctx.N):
                    row=exact_middle_double_star_fibre(ctx,e)
                    self.assertEqual(row['e'],e)
                    self.assertEqual(row['original_double_star_incidence_count'],
                                     row['independent_original_line_pencil_count'])
                    self.assertLessEqual(
                        row['original_double_star_incidence_count'],
                        row['original_spectral_upper_floor'])
                    self.assertLessEqual(
                        row['exact_integer_expander_mixing_lhs'],
                        row['exact_integer_expander_mixing_rhs'])
                    self.assertIn(e,row['original_double_star_incidence_ids'])
                    self.assertEqual(row['physical_coordinate_corner_count'],4)
                    self.assertLessEqual(row['true_original_point_star_size'],2*ctx.a-3)
                    self.assertLessEqual(row['true_original_line_star_size'],2*ctx.a-3)
                    all_rows.append(row)
                self.assertEqual(len(all_rows),ctx.N)
                self.assertGreater(max(x['original_double_star_incidence_count']
                                       for x in all_rows),0)

    def test_H2_original_forest_and_actual_middle_ID_band_contains_all_arms(self):
        for power,scheme in ((1,'lex'),(2,'lex'),(2,'random')):
            ctx=EndpointEnergy(fixture(power,scheme))
            result=FiveSourceSearch(fixture(power,scheme)).census(
                export_true_five_source_families=True)
            families=result['TRUE_ORIGINAL_five_source_families']
            if power==2:
                self.assertGreater(len(families),0)
            middle_cache={}
            for row in families:
                ids=tuple(row['original_incidence_ids'])
                self.assertEqual(len(ids),5)
                topology=source_forest_signature(ctx,ids)
                self.assertTrue(topology['acyclic_original_forest'])
                self.assertEqual(topology['edge_count'],5)
                self.assertEqual(
                    topology['original_point_count']+
                    topology['original_line_count']-
                    topology['original_components'],5)
                self.assertEqual(topology['original_point_degree_sequence'],
                                 (1,1,1,1,1))
                self.assertEqual(topology['original_line_degree_sequence'],
                                 (1,1,1,1,1))
                self.assertEqual(topology['original_components'],5)
                self.assertTrue(row['original_middle_source_ids'])
                for e in row['original_middle_source_ids']:
                    if e not in middle_cache:
                        middle_cache[e]=exact_middle_double_star_fibre(ctx,e)
                    self.assertTrue(
                        set(ids).issubset(
                            middle_cache[e]['original_double_star_incidence_ids']))
            with self.assertRaisesRegex(ValueError,'unique nonempty'):
                source_forest_signature(ctx,[0,0,1,2,3])

    def test_H3_distinct_real_five_source_middle_source_fibres_W34(self):
        for scheme,expected in (('lex',467),('random',575)):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                data=finite_fibre_and_family_report(model)
                self.assertEqual(data['source_families_distinct'],expected)
                self.assertEqual(data['oriented_true_four_blocked_squares'],
                                 expected*2)
                self.assertGreater(data[
                    'distinct_middle_sources_with_blocked_families'],0)
                self.assertGreater(data[
                    'maximum_distinct_five_families_per_middle_original_incidence'],0)
                self.assertLessEqual(data[
                    'max_spectral_source_fibre_size_used_by_blocked_family'],
                    data['max_spectral_source_fibre_size_ALL_true_middle_incidences'])
                self.assertEqual(sum(data['source_forest_profiles'].values()),expected)
                self.assertTrue(data[
                    'H2_all_blocked_five_source_families_true_original_matchings_verified'])
                self.assertEqual(len(data['source_forest_profiles']),1)
                self.assertFalse(data['empirical_middle_fibre_uniform_o_s4_cap_proved'])
                self.assertFalse(data['universal_GF5_sixset_transfer_proved'])

    def test_H2_matching_restriction_is_NOT_all_five_original_GQ_edges(self):
        # Arbitrary true source incidences can share a GQ point. The
        # stronger matching is asserted ONLY for actual coherent physical
        # 2x2 NB3 source footprints, never for all five-edge GQ forests.
        ctx=EndpointEnergy(fixture(2,'lex'))
        original_p=0
        lines=sorted(ctx.point_lines[original_p])
        self.assertEqual(len(lines),5)
        ids=[ctx.edge_id[original_p,l] for l in lines]
        topology=source_forest_signature(ctx,ids)
        self.assertTrue(topology['acyclic_original_forest'])
        self.assertEqual(topology['original_point_degree_sequence'],(5,))
        self.assertEqual(topology['original_line_degree_sequence'],(1,1,1,1,1))
        self.assertEqual(topology['original_components'],1)

    def test_H3_W32_finite_absence_is_only_map_specific(self):
        for scheme in ('lex','reverse','S68','S72'):
            row=finite_fibre_and_family_report(fixture(1,scheme))
            self.assertEqual(row['source_families_distinct'],0)
            self.assertEqual(row['distinct_middle_sources_with_blocked_families'],0)
            self.assertEqual(row[
                'maximum_distinct_five_families_per_middle_original_incidence'],0)
            self.assertFalse(row['root_Branch_A_proved'])

    def test_H3_all_h_heavy_original_middle_source_necessary_only(self):
        for s,theta in ((2**22,Fraction(1)),
                        (2**26,Fraction(1,2)),
                        (2**26,Fraction(7,8))):
            row=necessary_heavy_middle_five_source(s,theta)
            previous=conditional_all_h_distinct_five_source_lower(s,theta)
            self.assertEqual(
                Fraction(row['heavy_middle_distinct_five_family_count_lower']),
                Fraction(previous['distinct_true_original_five_incidence_sets_lower'])/
                row['true_original_incidence_count'])
            self.assertEqual(row['true_original_incidence_count'],
                             (s+1)**2*(s*s+1))
            self.assertFalse(row['proposed_uniform_o_s4_middle_source_upper_proved'])
            self.assertFalse(row['root_Branch_A_proved'])
        with self.assertRaisesRegex(ValueError,'exact stationary'):
            necessary_heavy_middle_five_source(64,Fraction(1))

    def test_fail_closed_source_labels_and_no_spectral_GQ_invention(self):
        ctx=EndpointEnergy(fixture(1,'lex'))
        with self.assertRaisesRegex(ValueError,'true middle ORIGINAL'):
            exact_middle_double_star_fibre(ctx,-1)
        with self.assertRaisesRegex(ValueError,'invalid true original incidence'):
            source_forest_signature(ctx,[999])
        bad=fixture(1,'lex')
        bad['left_labels']=list(bad['left_labels'])
        bad['left_labels'][0]=bad['left_labels'][1]
        with self.assertRaisesRegex(ValueError,'global injective'):
            finite_fibre_and_family_report(bad)

    def test_report_research_only_source_GF5_gate(self):
        data=report()
        self.assertEqual(data['status'],'RESTRICTED_THEOREM_H')
        self.assertEqual(data['root_A'],'OPEN')
        self.assertEqual(len(data['maps']),6)
        self.assertEqual(data['maps'][4]['source_families_distinct'],467)
        self.assertEqual(data['maps'][5]['source_families_distinct'],575)
        self.assertTrue(all(not row['root_Branch_A_proved']
                            for row in data['maps']))


if __name__=='__main__':
    unittest.main()
