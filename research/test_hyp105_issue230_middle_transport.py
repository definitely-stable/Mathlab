"""EICE-003-C: independent original provenance, Gram and marginal falsifiers."""
from collections import Counter
from fractions import Fraction
import unittest

from hyp105_issue230_anchor_lift import AnchorLiftedEnergy
from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_middle_transport import (
    OriginalMiddleTransport, midpoint_only_no_go,
    original_overlap, original_overlap_gram, report
)
from hyp105_issue230_paired_gstar import paired_gstar
from hyp105_issue230_projection import fixture


class OriginalMiddleTransportTests(unittest.TestCase):
    def test_all_four_true_W32_source_transport_equals_independent_B3(self):
        for scheme in ('lex','reverse','S68','S72'):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                row=OriginalMiddleTransport(model).census(independent_oracle=True)
                old=AnchorLiftedEnergy(model).census()
                self.assertEqual(row['original_incidence_total'],45)
                self.assertEqual(row['original_midpoint_source_count'],45)
                self.assertEqual(Fraction(row['theta_internal_only']),
                                 Fraction(old['theta_internal_only']))
                self.assertEqual(Fraction(row['true_left_overlap_mass']),
                                 Fraction(old['theta_left']))
                self.assertEqual(Fraction(row['true_right_overlap_mass']),
                                 Fraction(old['theta_right']))
                self.assertEqual(Fraction(row['true_double_lr_mass']),
                                 Fraction(old['simultaneous_left_right_internal']))
                self.assertEqual(Fraction(row['original_middle_equals_anchor_point']),
                                 Fraction(old['middle_source_double_left']))
                self.assertEqual(Fraction(row['original_middle_equals_anchor_line']),
                                 Fraction(old['middle_source_double_right']))
                self.assertEqual(Fraction(row['C2_exact_identity_rhs']),
                                 Fraction(row['theta_internal_only']))
                self.assertEqual(Fraction(row['C4_exact_total']),
                                 Fraction(row['theta_internal_only']))
                self.assertFalse(row['root_Branch_A_proved'])
                self.assertFalse(row['middle_uniform_alone_proves_gap'])
                self.assertLessEqual(row['max_original_source_blocked_row'],
                                     row['original_source_row_bound'])

    def test_independent_original_Ka_gram_point_line_factorization(self):
        for scheme in ('lex','S68'):
            model=fixture(1,scheme)
            ctx=EndpointEnergy(model)
            for labels in (ctx.f,ctx.g):
                for p,a in enumerate(labels):
                    n=0
                    for q,b in enumerate(labels):
                        direct=int(bool(set(a)&set(b)))
                        gram=original_overlap_gram(a,b,p==q)
                        self.assertEqual(direct,gram)
                        self.assertEqual(direct,original_overlap(a,b))
                        n+=direct
                    self.assertLessEqual(n,2*ctx.a-3)
            self.assertGreater(ctx.v,ctx.a)  # nontrivial -1 eigenspace

    def test_stationary_original_midpoint_uniformity_full_W32(self):
        for scheme in ('lex','reverse','S68','S72'):
            ctx=EndpointEnergy(fixture(1,scheme))
            row=OriginalMiddleTransport(fixture(1,scheme)).census()
            active_min=min((d for d in ctx.degree if d),default=0)
            if active_min>=2:
                self.assertTrue(row['stationary_midpoint'])
                self.assertFalse(row['conditioned_survival'])
                self.assertEqual(Fraction(row['raw_nb_weight']),2*row['physical_edges'])
            else:
                self.assertFalse(row['stationary_midpoint'])

    def test_real_W34_full_original_source_endpoints(self):
        for scheme in ('lex','random'):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                row=OriginalMiddleTransport(model).census(
                    max_paths=1_000_000,independent_oracle=True)
                old=AnchorLiftedEnergy(model).census(max_paths=1_000_000)
                self.assertEqual(row['original_incidence_total'],425)
                self.assertEqual(row['original_midpoint_source_count'],425)
                self.assertEqual(Fraction(row['theta_internal_only']),
                                 Fraction(old['theta_internal_only']))
                self.assertEqual(Fraction(row['true_double_lr_mass']),
                                 Fraction(old['simultaneous_left_right_internal']))
                self.assertGreaterEqual(Fraction(row['C4_signed_original_transport']),
                                        -Fraction(1))
                self.assertLessEqual(row['max_original_source_blocked_row'],
                                     row['original_source_row_bound'])

    def test_true_paired_Gstar_properness_and_source_pair_coherence(self):
        for scheme in ('lex','reverse','S68','S72'):
            model=fixture(1,scheme)
            selected=paired_gstar(model)['original_incidence_ids']
            try:
                row=OriginalMiddleTransport(model,selected=selected).census(
                    require_proper=True,independent_oracle=True)
            except ValueError as ex:
                self.assertIn('no nonbacktracking length-three paths',str(ex))
                continue
            self.assertEqual(row['improper_nb_walks'],0)
            self.assertEqual(row['physical_edges'],2*len(selected))
            self.assertEqual(Fraction(row['theta_internal_only']),
                Fraction(AnchorLiftedEnergy(model,selected=selected).census(
                    require_proper=True)['theta_internal_only']))

    def test_midpoint_only_relaxation_is_not_a_path_counterexample(self):
        for scheme in ('lex','reverse','S68','S72'):
            witness=midpoint_only_no_go(fixture(1,scheme))
            self.assertTrue(witness['every_middle_point_equals_true_anchor_point'])
            self.assertEqual(witness['true_original_middle_sources'],45)
            self.assertEqual(Fraction(witness['uniform_middle_marginal_each']),
                             Fraction(1,45))
            self.assertEqual(Fraction(witness['relaxed_internal_overlap_mass']),1)
            self.assertFalse(witness['actual_branch_A_counterexample'])
            self.assertIn('no end-clean or true physical NB3',witness['label'])

    def test_stationary_leaf_and_bad_global_injection_rejected(self):
        model=fixture(1,'lex')
        with self.assertRaisesRegex(ValueError,'min-degree'):
            OriginalMiddleTransport(model,selected=[0]).census(
                require_stationary=True)
        with self.assertRaisesRegex(ValueError,'walk budget'):
            OriginalMiddleTransport(model).census(max_paths=0)
        bad=fixture(1,'lex')
        bad['left_labels']=list(bad['left_labels'])
        bad['left_labels'][0]=bad['left_labels'][1]
        with self.assertRaisesRegex(ValueError,'global injective'):
            OriginalMiddleTransport(bad)

    def test_standalone_report_honest_root_gate(self):
        data=report()
        self.assertEqual(data['root_A'],'OPEN')
        self.assertEqual(data['status'],'RESTRICTED_THEOREM_C')
        self.assertEqual(len(data['results']),8)


if __name__=='__main__':
    unittest.main()
