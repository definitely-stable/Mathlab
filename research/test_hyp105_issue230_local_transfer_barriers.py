"""Independent finite falsifiers for the scoped issue230 local barriers."""
from contextlib import redirect_stdout
from importlib import import_module, util
from io import StringIO
from pathlib import Path
import json
import tempfile
import unittest


class LocalTransferBarrierTests(unittest.TestCase):
    def module(self, name):
        self.assertIsNotNone(util.find_spec(name), f"portable oracle missing: {name}")
        return import_module(name)

    def test_global_minimal_W38_maps_have_784_local_families_not_dense_Gstar(self):
        m = self.module('hyp105_issue230_local_capacity_barrier')
        field, model, data = m.construct(3, 8)
        report = m.validate(field, model, data)
        self.assertEqual(report['a'], 35)
        self.assertEqual(len(set(model['left_labels'])), 585)
        self.assertEqual(len(set(model['right_labels'])), 585)
        self.assertEqual(report['all_blocked_distinct_five_source_sets_at_one_middle'], 784)
        self.assertEqual(report['all_blocked_oriented_squares'], 1568)
        self.assertEqual(report['proper_NB3_paths'], 128)
        self.assertEqual(report['local_min_active_degree'], 1)
        self.assertEqual(report['paired_physical_edges'], 34)
        self.assertFalse(report['high_degree_EICE002_Gstar'])

    def test_W34_small_realization_and_invalid_global_injection(self):
        m = self.module('hyp105_issue230_local_capacity_barrier')
        field, model, data = m.construct(2, 2)
        self.assertEqual(m.validate(field, model, data)[
            'all_blocked_distinct_five_source_sets_at_one_middle'], 1)
        bad = dict(model, right_labels=model['right_labels'][:-1])
        with self.assertRaisesRegex(ValueError, 'global injective'):
            m.validate(field, bad, data)

    def test_eighteen_sources_have_ten_improper_cycles_but_no_selected_sixset(self):
        m = self.module('hyp105_issue230_local_cycle_barrier')
        pattern = self.module('hyp105_issue230_local_cycle_pattern')
        items = m.source_patch()
        counts, leafless = m.direct_original_sixsets(items)
        self.assertEqual(sum(counts.values()), 0)
        self.assertEqual(len(leafless), 2)
        adj, _ = pattern.build_graph([e[:3] for e in items])
        cycles = pattern.graph_cycles(adj, 6)
        self.assertEqual(len(cycles), 10)
        self.assertFalse(pattern.graph_cycles(adj, 4))
        self.assertTrue(all(len({x for edge in c for x,y in edge}) < 6 or
                            len({y for edge in c for x,y in edge}) < 6
                            for c in cycles))

    def test_cycle_patch_has_independent_true_GQ_embedding_and_full_maps(self):
        m = self.module('hyp105_issue230_local_cycle_barrier')
        result = m.real_source_embedding(m.source_patch())
        self.assertEqual(result['source_point_count'], 585)
        self.assertEqual(result['source_line_count'], 585)
        self.assertEqual(result['complete_f_size'], 585)
        self.assertEqual(result['complete_g_size'], 585)
        self.assertEqual(result['induced_selected_incidence_count'], 18)
        self.assertEqual(result['a_minimal'], 35)

    def test_quadratic_planes_equal_independent_source_Pluecker_pencils(self):
        m = self.module('hyp105_issue230_geometric_duad_barriers')
        for h, expected in ((1, 15), (2, 85)):
            _, direct = m.direct_quadratic_planes(h)
            original = m.true_source_planes(h)
            self.assertEqual(len(direct), expected)
            self.assertEqual(direct, original)

    def test_exact_spectral_capacity_on_every_W32_subset(self):
        m = self.module('hyp105_issue230_geometric_duad_barriers')
        self.assertEqual(m.all_w32_subsets_spectral_bound(), 32768)
        for h in range(1, 13):
            p = m.palette_arithmetic(h)
            self.assertLess(p['literal_source_duad_line_upper'], p['V'])

    def test_original_11663_partition_ledger_keeps_physical_polynomials_separate(self):
        m = self.module('hyp105_issue230_partition_index')
        with tempfile.TemporaryDirectory() as tmp, redirect_stdout(StringIO()):
            m.main(output_dir=Path(tmp))
            report = json.loads((Path(tmp)/'partition-index-results.json').read_text())
            polynomials = json.loads((Path(tmp)/'physical_projection_polynomials.json').read_text())
            self.assertEqual(report['stratum_counts'], {'leading':631, 'subleading_necessary':11032})
            self.assertEqual(report['source_partition_pairs_checked_by_two_forest_methods'], 41209)
            self.assertEqual(report['ledger_sha256'],
                             '9bdf2652ef0ce211c739c6b1dc39702c3656e984c821674a51372dd9cfc04b7a')
            self.assertEqual(len(polynomials), 11)


if __name__ == '__main__':
    unittest.main()
