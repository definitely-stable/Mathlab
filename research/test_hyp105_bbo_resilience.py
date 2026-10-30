"""True-source exposure, weighted loss, and six-ID avoidance controls."""
import json
from pathlib import Path
import unittest

from hyp105_bbo_resilience import (
    source_exposure_geometry, exposure_certificate, avoidance_certificate,
    certificate_suite,
)
from hyp105_g5e2a_pair_embeddings import pair_labeled_symplectic
from hyp105_g5e2b3e1b0_seven_signature import seven_census


class BBoResilience(unittest.TestCase):
    def test_every_genuine_W32_W34_flag_has_three_disjoint_s_squared_roles(self):
        for power in (1, 2):
            s, _, flags, projections, postings = source_exposure_geometry(power)
            self.assertEqual(len(projections), len(flags)*s*s)
            for roles in postings:
                self.assertEqual(tuple(map(len, roles)), (s*s,)*3)
                self.assertEqual(len(set().union(*roles)), 3*s*s)

    def test_exposure_union_and_hits_count_for_source_subsets(self):
        for power in (1, 2):
            s, _, flags, _, _ = source_exposure_geometry(power)
            for ids in ((), (0,), tuple(range(s+1)), tuple(range(0, len(flags), 7)), tuple(range(len(flags)))):
                row = exposure_certificate(power, ids)
                self.assertLessEqual(row['exposed_typed_pairs'], row['union_bound_typed'])
                self.assertEqual(sum(int(k)*n for k, n in row['flag_hits_per_projection_histogram'].items()),
                                 3*s*s*len(ids))
            all_ids = exposure_certificate(power, range(len(flags)))
            self.assertEqual(all_ids['flag_hits_per_projection_histogram']['3'], len(flags)*s*s)

    def test_frozen_true_source_certificate(self):
        expected = json.loads((Path(__file__).parent/'fixtures/hyp105_bbo_resilience.json').read_text())
        actual = certificate_suite()
        self.assertEqual(actual, expected)
        self.assertTrue(all(not row['finite_check_proves_asymptotic_coefficient'] for row in actual.values()))
        self.assertGreater(actual['W34_sparse_spread']['surviving_paths_with_anchor_outside_core'], 0)
        self.assertGreater(actual['W34_sparse_singleton']['unblocked_paths_rejected_for_forbidden_anchor'], 0)

    def test_independent_COMPLETE_W32_original_seven_class_census(self):
        model = pair_labeled_symplectic(1, 'lex')
        # This source-template census does not enumerate physical 3-paths.
        census = seven_census(model, independent_checks=False, witness_sets=True)
        for forbidden in ((), (2,), (0, 1, 2), (10, 20, 30)):
            row = avoidance_certificate(1, model['left_labels'], model['right_labels'], forbidden)
            whole_class = {ids for ids, tag in census['sets'].items()
                           if tag == 'B/B-overlap' and not set(ids).intersection(forbidden)}
            produced = set(map(tuple, row['produced_sixsets']))
            self.assertLessEqual(produced, whole_class)
            self.assertEqual(2*len(produced), row['unblocked_paths_avoiding_all_six_forbidden_ids'])

    def test_coordinate_permutation_and_reject_invalid_ids_and_core(self):
        model = pair_labeled_symplectic(1, 'lex')
        f, g = model['left_labels'], model['right_labels']
        baseline = avoidance_certificate(1, f, g, (2,))
        ff = [tuple(sorted((5*x+1) % 6 for x in pair)) for pair in f]
        gg = [tuple(sorted((5*x+3) % 6 for x in pair)) for pair in g]
        self.assertEqual(baseline, avoidance_certificate(1, ff, gg, (2,)))
        for bad in ((True,), (45,), (-1,), (0, 0)):
            with self.assertRaises(ValueError):
                avoidance_certificate(1, f, g, bad)
        with self.assertRaises(ValueError):
            avoidance_certificate(1, f, g, (2,), core_ids=(0, 2))
        with self.assertRaises(ValueError):
            avoidance_certificate(1, f[:-1], g)


if __name__ == '__main__':
    unittest.main()
