"""Definition-level checks of the universal P3 lemma's unresolved closure gate."""
from collections import Counter
from importlib import import_module, util
import unittest


class Issue230ProjectionTests(unittest.TestCase):
    def api(self):
        name = 'hyp105_issue230_projection'
        self.assertIsNotNone(util.find_spec(name), 'projection closure oracle missing')
        return import_module(name)

    def test_true_gq_cubic_identity_and_unique_nonincident_projection(self):
        api = self.api()
        from hyp105_issue230_proof_audit import frozen_model
        context = api.ProjectionClosure(frozen_model('lex'))
        counts = context.original_cubic_counts()
        self.assertEqual(len(context.projection), 15**2-45)
        for q in range(15):
            for r in range(15):
                self.assertEqual(counts[q, r], 5 if (q, r) in context.edge_id else 1)

    def test_exact_path_partition_and_synchronized_bbo_multiplicity(self):
        api = self.api()
        from hyp105_issue230_proof_audit import frozen_model
        from hyp105_g5e2b3e1b0_seven_signature import seven_census
        expected = {
            'lex': (1346, 400, 942, 4, 2),
            'reverse': (1154, 256, 898, 0, 0),
            'S68': (678, 72, 606, 0, 0),
            'S72': (738, 80, 658, 0, 0),
        }
        for scheme, values in expected.items():
            model = frozen_model(scheme)
            row = api.ProjectionClosure(model).census(collect_witnesses=True)
            self.assertEqual(tuple(row[k] for k in ('proper_P3', 'incident',
                             'blocked', 'unblocked', 'synchronized_BBo')), values)
            self.assertEqual(row['missing'], 0)
            self.assertEqual(row['proper_P3'], row['missing']+row['incident']+
                             row['blocked']+row['unblocked'])
            self.assertEqual(set(row['witness_multiplicities'].values()),
                             {2} if row['unblocked'] else set())
            accepted = seven_census(model, witness_sets=True)['sets']
            for six in row['witness_multiplicities']:
                self.assertEqual(accepted[six], 'B/B-overlap')
            # The synchronized family is only a subclass of the full BB-overlap.
            self.assertLessEqual(row['synchronized_BBo'],
                                 Counter(accepted.values())['B/B-overlap'])
            self.assertFalse(row['universal_S_lower_proved'])

    def test_walk_budget_and_global_pair_maps_fail_closed(self):
        api = self.api()
        from hyp105_issue230_proof_audit import frozen_model
        context = api.ProjectionClosure(frozen_model('lex'))
        with self.assertRaisesRegex(ValueError, 'path budget'):
            context.census(max_paths=1)
        model = frozen_model('lex')
        right = list(model['right_labels'])
        right[1] = right[0]
        model['right_labels'] = tuple(right)
        with self.assertRaises(ValueError):
            api.ProjectionClosure(model)

    def test_true_w34_global_map_closures_are_accepted_original_sixsets(self):
        api = self.api()
        model = api.fixture(2, 'random')
        row = api.ProjectionClosure(model).census(collect_witnesses=True)
        self.assertEqual(tuple(row[k] for k in ('proper_P3', 'missing', 'incident',
                         'blocked', 'unblocked', 'synchronized_BBo')),
                         (78894, 10198, 4112, 48542, 16042, 8021))
        self.assertEqual(len(row['witness_multiplicities']), 8021)
        for six, multiplicity in row['witness_multiplicities'].items():
            self.assertEqual(multiplicity, 2)
            self.assertEqual(len(set(six)), 6)
            endpoints = [tuple(model['incidences'][i][side] for i in six)
                         for side in (0, 1)]
            doubled = []
            for end, labels in zip(endpoints, (model['left_labels'], model['right_labels'])):
                freq = Counter(end)
                self.assertEqual(sorted(freq.values()), [1, 1, 1, 1, 2])
                deg = Counter(x for q in end for x in labels[q])
                self.assertEqual(len(deg), 6)
                self.assertEqual(set(deg.values()), {2})
                doubled.append(next(q for q, n in freq.items() if n == 2))
            positions = [{i for i, q in enumerate(end) if q == d}
                         for end, d in zip(endpoints, doubled)]
            self.assertEqual(len(positions[0] & positions[1]), 1)


if __name__ == '__main__':
    unittest.main()
