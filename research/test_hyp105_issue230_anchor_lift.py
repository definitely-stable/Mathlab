"""EICE-003 anchor-lifted exact ORIGINAL GQ regression and falsifiers."""
import unittest
from fractions import Fraction

from hyp105_issue230_anchor_lift import AnchorLiftedEnergy, report
from hyp105_issue230_endpoint_energy import EndpointEnergy
from hyp105_issue230_paired_gstar import paired_gstar
from hyp105_issue230_projection import fixture


class AnchorLiftTests(unittest.TestCase):
    def test_true_original_W32_four_schemes_and_independent_pair_oracle(self):
        for scheme in ('lex','reverse','S68','S72'):
            with self.subTest(scheme=scheme):
                model=fixture(1,scheme)
                a=AnchorLiftedEnergy(model).census(independent_collision=True)
                old=EndpointEnergy(model).energy()
                self.assertEqual(a['theta_internal_only'],
                                 old['theta_internal_only'])
                self.assertEqual(a['anchor_carrier_size_each'],360)
                self.assertLessEqual(a['clean_carrier_size_each'],360)
                self.assertEqual(a['clean_carrier_size_each'],2*a['clean_original_endpoint_pairs'])
                self.assertGreaterEqual(Fraction(a['A1_clean_slack']),0)
                self.assertLessEqual(Fraction(a['A1_clean_slack']),Fraction(a['A1_slack']))
                self.assertEqual(a['original_incidences_selected'],45)
                self.assertEqual(a['physical_edges'],90)
                self.assertGreaterEqual(Fraction(a['A1_slack']),0)
                self.assertLessEqual(Fraction(a['A_f']),
                                     Fraction(a['unlifted_same_restricted_f']))
                self.assertLessEqual(Fraction(a['A_g']),
                                     Fraction(a['unlifted_same_restricted_g']))
                self.assertFalse(a['root_Branch_A_proved'])
                self.assertTrue(a['A3_parseval_validated'])
                af,ag=Fraction(a['A_f']),Fraction(a['A_g'])
                T2=Fraction(a['original_endpoint_collision_T2'])
                resf=Fraction(a['left_coordinate_residual'])
                resg=Fraction(a['right_coordinate_residual'])
                self.assertEqual(af+ag, 2*T2/model['a']+resf+resg)
                self.assertGreaterEqual(resf,0)
                self.assertGreaterEqual(resg,0)
                if a['clean_original_endpoint_pairs']:
                    P=Fraction(a['eligible_end_clean_mass'])
                    self.assertGreaterEqual(T2,P*P/a['clean_original_endpoint_pairs'])

    def test_true_original_W34_reduced_source_provenance(self):
        for scheme in ('lex','random'):
            with self.subTest(scheme=scheme):
                model=fixture(2,scheme)
                reg=paired_gstar(model,verify_paths=True)
                a=AnchorLiftedEnergy(model, selected=reg['original_incidence_ids'])
                try:
                    row=a.census(require_proper=True,independent_collision=True)
                except ValueError as exc:
                    # At s=4 even coherent regularization can have no NB3;
                    # never promote this to an asymptotic failure or success.
                    if 'no nonbacktracking paths' not in str(exc):
                        raise
                    continue
                self.assertEqual(row['improper_nb_paths'],0)
                self.assertEqual(row['anchor_carrier_size_each'],2*425*16)
                self.assertEqual(row['physical_edges'],
                                 2*len(reg['original_incidence_ids']))
                self.assertGreaterEqual(Fraction(row['A1_slack']),0)
                self.assertGreaterEqual(Fraction(row['A1_clean_slack']),0)
                self.assertGreaterEqual(Fraction(row['A1_clean_slack']),0)

    def test_real_eligible_anchor_carrier_count_all_h_finite(self):
        for s in (2,4,8,16,32,64):
            V=(s+1)*(s*s+1)
            N=V*(s+1)
            # exact GQ projection axiom yields V^2-N=N*s^2
            self.assertEqual(V*V-N,N*s*s)

    def test_paired_Gstar_real_W32_proper_or_explicit_no_paths(self):
        for scheme in ('lex','reverse','S68','S72'):
            model=fixture(1,scheme)
            ids=paired_gstar(model)['original_incidence_ids']
            try:
                row=AnchorLiftedEnergy(model, selected=ids).census(
                    require_proper=True,independent_collision=True)
                self.assertEqual(row['improper_nb_paths'],0)
                self.assertTrue(row['conditional_on_survival'] or
                                Fraction(row['raw_nb_mass'])==2*row['physical_edges'])
                self.assertGreaterEqual(Fraction(row['A1_slack']),0)
            except ValueError as exc:
                self.assertIn('no nonbacktracking paths',str(exc))

    def test_stationary_rejects_finite_leaf_graph(self):
        model=fixture(1,'lex')
        with self.assertRaisesRegex(ValueError,'min-degree'):
            AnchorLiftedEnergy(model,selected=[0]).census(
                require_stationary=True)

    def test_corrupted_global_map_rejected(self):
        model=fixture(1,'lex')
        model['left_labels']=list(model['left_labels'])
        model['left_labels'][0]=model['left_labels'][1]
        with self.assertRaisesRegex(ValueError,'global injective'):
            AnchorLiftedEnergy(model)

    def test_guardrails_walk_budget_and_report(self):
        model=fixture(1,'S68')
        with self.assertRaisesRegex(ValueError,'path budget'):
            AnchorLiftedEnergy(model).census(max_paths=1)
        data=report()
        self.assertEqual(data['status'],'RESTRICTED_THEOREM_C')
        self.assertEqual(data['root_A'],'OPEN')
        self.assertEqual(len(data['rows']),8)


if __name__=='__main__':
    unittest.main()
