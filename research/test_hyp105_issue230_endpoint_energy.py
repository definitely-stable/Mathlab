"""Finite ORIGINAL W32 exact rational collision energy falsifiers."""
import unittest
from fractions import Fraction

from hyp105_issue230_endpoint_energy import EndpointEnergy, report
from hyp105_issue230_projection import fixture


class EndpointCollisionEnergyTests(unittest.TestCase):
    def test_four_true_original_global_injections_and_independent_collision_oracle(self):
        for scheme in ('lex', 'reverse', 'S68', 'S72'):
            with self.subTest(scheme=scheme):
                context = EndpointEnergy(fixture(1, scheme))
                row = context.energy(independent_oracle=True)
                self.assertEqual(row['original_incidences'], 45)
                self.assertEqual(row['selected_original_incidences'], 45)
                self.assertEqual(row['physical_edges'], 90)
                self.assertEqual(row['necessary_threshold_fraction'], '1/16')
                self.assertGreater(row['nonbacktracking_walks'], 0)
                self.assertLessEqual(Fraction(row['theta_internal_only']),
                                     Fraction(row['theta_W']))
                self.assertLessEqual(
                    Fraction(row['theta_W'])**2,
                    16*45*(Fraction(row['E_f'])+Fraction(row['E_g'])))
                self.assertFalse(row['universal_S_lower_proved'])

    def test_full_graph_not_promoted_to_regularized_G_star(self):
        data = report()
        self.assertEqual(data['status'], 'RESTRICTED_THEOREM_C')
        self.assertIn('NOT regularized G*', data['scope'])
        self.assertEqual([r['scheme'] for r in data['records']],
                         ['lex', 'reverse', 'S68', 'S72'])

    def test_corrupt_global_label_fails_closed(self):
        model = fixture(1, 'lex')
        model['right_labels'] = list(model['right_labels'])
        model['right_labels'][0] = model['right_labels'][1]
        with self.assertRaisesRegex(ValueError, 'global injective'):
            EndpointEnergy(model)

    def test_subset_rejects_repeated_or_invalid_incidence_ids(self):
        model = fixture(1, 'lex')
        with self.assertRaisesRegex(ValueError, 'distinct genuine incidence'):
            EndpointEnergy(model, selected=[0, 0])
        with self.assertRaisesRegex(ValueError, 'genuine incidence'):
            EndpointEnergy(model, selected=[-1])

    def test_path_budget_fails_closed(self):
        with self.assertRaisesRegex(ValueError, 'path budget'):
            EndpointEnergy(fixture(1, 'lex')).energy(max_paths=1)

    def test_exact_source_coordinate_capacity_on_original_GQ(self):
        context = EndpointEnergy(fixture(1, 'lex'))
        self.assertLessEqual(len(context.Cf), 2*context.N)
        self.assertLessEqual(len(context.Cg), 2*context.N)
        for r, x in context.Cf:
            self.assertTrue(any(x in context.f[q] for q in context.line_points[r]))
        for q, y in context.Cg:
            self.assertTrue(any(y in context.g[r] for r in context.point_lines[q]))

    def test_selected_source_incidence_keeps_both_physical_diagonals(self):
        context = EndpointEnergy(fixture(1, 'S68'), selected=[0, 2, 5])
        self.assertEqual(context.m, 6)
        self.assertEqual(set(context.provenance.values()), {0, 2, 5})
        with self.assertRaisesRegex(ValueError, 'min-degree'):
            context.energy(require_min_degree_two=True)


if __name__ == '__main__':
    unittest.main()
