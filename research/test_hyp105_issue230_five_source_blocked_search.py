"""EICE-003-G: true ORIGINAL five-source blocked K22 witness search."""
from fractions import Fraction
import random
import unittest

from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_source_plaquettes import OriginalPlaquette
from hyp105_issue230_four_anchor_capacity import find_true_nonvacuous_w32
from hyp105_issue230_five_source_blocked_search import (
    FiveSourceSearch, five_source_ids, exact_five_source_coherence,
    conditional_no_local_square_theta_bound,
)
from hyp105_issue230_paired_gstar import paired_gstar
from hyp105_issue230_projection import fixture


class FiveSourceBlockedSearchTests(unittest.TestCase):
    def test_localization_true_five_source_and_paired_diagonals(self):
        model=fixture(1,'lex')
        witness=find_true_nonvacuous_w32(model)
        self.assertEqual(len(witness['selected']),5)
        coherent=exact_five_source_coherence(model,witness['selected'])
        self.assertIsNotNone(coherent)
        o,cl,cr=coherent
        self.assertEqual(len(o.ctx.provenance),10)
        self.assertEqual(len(o.ctx.selected),5)
        row=o.census()
        self.assertGreater(row['total_2x2_plaquettes'],0)
        self.assertGreater(row['original_endpoint_complete_plaquettes'],0)
        self.assertEqual(row['all_four_internally_blocked_plaquettes'],0)
        self.assertIsNone(exact_five_source_coherence(model,range(4)))
        self.assertIsNone(exact_five_source_coherence(model,(0,0,1,2,3)))

    def test_all_four_frozen_W32_global_injection_maps_exhaustive(self):
        for scheme in ('lex','reverse','S68','S72'):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                ctx=EndpointEnergy(model)
                row=FiveSourceSearch(model).census(independent_witness_oracle=True)
                self.assertEqual(row['oriented_middle_edges_examined'],2*ctx.m)
                self.assertEqual(row['original_incidences'],45)
                self.assertGreaterEqual(
                    row['raw_allfour_blocked_plaquettes_before_coherence'],
                    row['locally_coherent_allfour_original_plaquettes'])
                self.assertGreaterEqual(
                    row['raw_allfour_with_five_distinct_original_source_ids'],
                    row['locally_coherent_allfour_original_plaquettes'])
                self.assertEqual(row['finite_map_no_coherent_allblocked_square'],
                                 row['locally_coherent_allfour_original_plaquettes']==0)
                self.assertFalse(row['universal_all_h_forbidden_five_source_theorem_proved'])
                self.assertFalse(row['bounded_multiplicity_GF5_transfer_proved'])
                for witness in row['witnesses']:
                    self.assertEqual(len(witness['original_source_incidence_ids']),5)
                    self.assertTrue(witness['same_five_source_pair_diagonals'])
                    self.assertTrue(witness['independent_restricted_F_oracle_verified'])

    def test_original_W34_lex_random_maps_complete_local_scan(self):
        for scheme in ('lex','random'):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                ctx=EndpointEnergy(model)
                row=FiveSourceSearch(model).census(
                    max_middle_orientations=4_000,
                    max_physical_nb3_cells=3_000_000,
                    max_allblocked_candidates=150_000,
                    independent_witness_oracle=True)
                self.assertEqual(row['oriented_middle_edges_examined'],2*ctx.m)
                self.assertEqual(row['original_incidences'],425)
                self.assertFalse(row['branch_A_proved'])

    def test_frozen_W32_deterministic_shuffled_original_line_maps(self):
        # Actual globally injected ORIGINAL GQ models, not abstract
        # transport laws; eight adversarial physical-pair permutations.
        base=fixture(1,'lex')
        for seed in range(8):
            with self.subTest(seed=seed):
                model=dict(base)
                model['left_labels']=list(base['left_labels'])
                model['right_labels']=list(base['right_labels'])
                random.Random(230_000+seed).shuffle(model['right_labels'])
                row=FiveSourceSearch(model).census()
                self.assertEqual(row['original_incidences'],45)
                self.assertEqual(row['oriented_middle_edges_examined'],180)
                self.assertEqual(row['finite_map_no_coherent_allblocked_square'],
                                 not bool(row['locally_coherent_allfour_original_plaquettes']))

    def test_analytic_if_absence_fourth_power_bound_and_fail_closed(self):
        for d in (3,4,100,2_000_000):
            r=conditional_no_local_square_theta_bound(d,False)
            self.assertEqual(Fraction(r['theta_I_fourth_power_upper']),
                             Fraction(2,d-1))
            self.assertFalse(r['universal_exclusion_of_allblocked_plaquettes_proved'])
            self.assertFalse(r['branch_A_proved'])
        with self.assertRaisesRegex(ValueError,'active degree'):
            conditional_no_local_square_theta_bound(2,False)
        with self.assertRaisesRegex(ValueError,'cannot assert'):
            conditional_no_local_square_theta_bound(4,True)

    def test_invalid_source_and_exhaustiveness_budgets(self):
        model=fixture(1,'lex')
        ctx=EndpointEnergy(model)
        u=next(u for u,ns in enumerate(ctx.adj) if ns)
        v=next(iter(ctx.adj[u]))
        with self.assertRaisesRegex(ValueError,'genuine distinct'):
            five_source_ids(ctx,u,v,(u,u),(v,v))
        with self.assertRaisesRegex(ValueError,'middle-orientation budget'):
            FiveSourceSearch(model).census(max_middle_orientations=0)
        with self.assertRaisesRegex(ValueError,'nonnegative integer'):
            FiveSourceSearch(model).census(max_allblocked_candidates=-1)
        bad=fixture(1,'lex')
        bad['left_labels']=list(bad['left_labels'])
        bad['left_labels'][0]=bad['left_labels'][1]
        with self.assertRaisesRegex(ValueError,'global injective'):
            FiveSourceSearch(bad)

    def test_independent_prior_gstar_w32_inclusion(self):
        # Any actual selected canonical G* 4-blocked square would have
        # to show up in the COMPLETE five-source physical enumeration.
        # Cross-check on the true selected finite graphs.
        for scheme in ('lex','reverse','S68','S72'):
            model=fixture(1,scheme)
            selected=paired_gstar(model)
            row=OriginalPlaquette(
                model,selected['original_incidence_ids'],
                selected['colors_left'],selected['colors_right']).census()
            full=FiveSourceSearch(model).census()
            if row['all_four_internally_blocked_plaquettes']:
                self.assertGreater(full['locally_coherent_allfour_original_plaquettes'],0)
            self.assertEqual(row['all_four_internally_blocked_plaquettes'],0)
            self.assertFalse(full['branch_A_proved'])


if __name__=='__main__':
    unittest.main()
