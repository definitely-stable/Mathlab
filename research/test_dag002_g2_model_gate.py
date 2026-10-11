"""Independent DAG-002 G2-A model and source-gate regressions."""
from __future__ import annotations

import unittest

from dag002_g2_model_gate import (
    cross_history_prefix_pair, insert_old_edge, lazy_append, lazy_query,
    ordered_dags, reach, run_report, sources,
)


class SourceGateTests(unittest.TestCase):
    def test_primary_source_keys_and_audit_levels(self):
        table = sources()
        self.assertEqual(table["proof_status"], "NOVELTY_UNPROVED")
        self.assertIs(table["source_proof_replay"], False)
        refs = {s["key"]: s for s in table["sources"]}
        self.assertEqual(len(refs), len(table["sources"]))
        self.assertGreaterEqual(len(refs), 12)
        for key in ("sea2025", "tcc2014", "bitprobe2007", "larsenyu2025",
                    "ko2025", "ko2026", "natural2026", "tasboneh2023",
                    "accumulator2026", "reachsurvey2025", "covering1986"):
            self.assertIn(key, refs)
        for src in refs.values():
            self.assertTrue(src["url"].startswith("https://"))
            self.assertTrue(src["restriction"])
            self.assertNotIn("PROVED_NOVEL", src["relation"])
            self.assertIn(src["evidence"], {
                "PUBLISHER_SCOPE_CHECKED", "AUTHOR_REPORT_ABSTRACT_CHECKED",
                "CONFERENCE_PROCEEDINGS_ABSTRACT_CHECKED", "ORIGINAL_IDENTITY_CHECKED",
            })

    def test_no_implicit_alphabet_or_output_transfer(self):
        refs = {s["key"]: s for s in sources()["sources"]}
        self.assertEqual(refs["sea2025"]["update"], "APPEND_SINK")
        self.assertEqual(refs["sea2025"]["query"], "BOOLEAN_REACHABILITY")
        self.assertEqual(refs["larsenyu2025"]["update"], "INSERT_OLD_EDGE")
        self.assertEqual(refs["larsenyu2025"]["relation"],
                         "NONTRANSFER_WITHOUT_REDUCTION")
        self.assertNotEqual(refs["rank2026"]["query"], "BOOLEAN_REACHABILITY")
        self.assertNotEqual(refs["ko2026"]["update"], "APPEND_SINK")
        self.assertIsNone(refs["ko2025"]["catalog_id"])
        self.assertEqual(refs["ko2026"]["catalog_id"], "LIT-119")

    def test_ordered_dag_exact_counts(self):
        for n in range(5):
            self.assertEqual(sum(1 for _ in ordered_dags(n)),
                             1 << (n * (n - 1) // 2))

    def test_append_no_old_old_effect_and_lazy_query_all_small_dags(self):
        for graph in ordered_dags(4):
            for mask in range(16):
                new, update_reads = lazy_append(
                    graph, tuple(p for p in range(4) if (mask >> p) & 1)
                )
                self.assertEqual(update_reads, 0)
                for source in range(4):
                    for target in range(4):
                        self.assertEqual(reach(graph, source, target),
                                         reach(new, source, target))
                for source in range(5):
                    for target in range(5):
                        got, reads = lazy_query(new, source, target)
                        self.assertEqual(got, reach(new, source, target))
                        self.assertLessEqual(reads, 5)

    def test_old_edge_insertion_different_update_alphabet(self):
        graph = ((), ())
        self.assertFalse(reach(graph, 0, 1))
        old_updated = insert_old_edge(graph, 0, 1)
        self.assertTrue(reach(old_updated, 0, 1))
        sink, _ = lazy_append(graph, (0,))
        self.assertFalse(reach(sink, 0, 1))
        self.assertTrue(reach(sink, 0, 2))

    def test_equal_next_command_prior_history_fiber(self):
        a, b = cross_history_prefix_pair()
        new_a, ra = lazy_append(a, (1,))
        new_b, rb = lazy_append(b, (1,))
        self.assertEqual((ra, rb), (0, 0))
        self.assertFalse(reach(new_a, 0, 2))
        self.assertTrue(reach(new_b, 0, 2))
        self.assertTrue(reach(new_a, 1, 2))
        self.assertTrue(reach(new_b, 1, 2))

    def test_reject_invalid_hidden_parent_input(self):
        graph = ((), ())
        for command in ((2,), (0, 0), (1, 0), (-1,)):
            with self.assertRaises(ValueError):
                lazy_append(graph, command)
        with self.assertRaises(ValueError):
            insert_old_edge(graph, 1, 0)

    def test_exact_report_without_theorem_promotion(self):
        r = run_report()
        self.assertEqual(r["append_cases"], 1024)
        self.assertEqual(r["lazy_query_cases"], 25600)
        self.assertFalse(r["source_proof_replay"])
        self.assertIn("NO_NOVEL_THEOREM", r["status"])


if __name__ == "__main__":
    unittest.main()
