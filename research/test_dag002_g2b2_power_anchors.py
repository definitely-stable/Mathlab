"""Finite source-definition tests for SEA 2025 power anchors (B>=2)."""
import unittest

from dag002_g2b2_power_anchors import (
    PowerAnchorIndex, five_vertex_power_census, highest_crossed_power
)
from dag002_g2b2_felsner import source_dfs


class PowerAnchorTests(unittest.TestCase):
    def test_all_1024_five_node_graphs_three_bases(self):
        report = five_vertex_power_census()
        self.assertEqual(report["traces"], 3072)
        self.assertEqual(report["queries"], 3072 * 55)

    def test_positive_crossed_multiple_definition(self):
        for base in (2, 3, 4, 10):
            for low in range(41):
                for high in range(low + 1, 42):
                    pi = highest_crossed_power(low, high, base)
                    powers = [e for e in range(42)
                              if high // base**e > low // base**e]
                    self.assertEqual(pi, max(powers), (base, low, high))
        with self.assertRaises(ValueError):
            highest_crossed_power(0, 1, 1)
        with self.assertRaises(ValueError):
            highest_crossed_power(1, 1, 2)

    def test_original_paper_path_2302_base10(self):
        db = PowerAnchorIndex(10)
        for v in range(2302):
            db.append((v - 1,) if v else ())
        self.assertEqual(db.labels[2299].rank, 2300)
        self.assertEqual(db.labels[2299].power, 2)
        self.assertEqual(db.labels[1999].power, 3)
        self.assertEqual(db.labels[2301].rank, 2302)
        self.assertLessEqual(db.anchor_depth(2301), 32)
        for u, v in ((0, 2301), (30, 2301), (999, 2301),
                     (2100, 2301), (2301, 2301)):
            self.assertTrue(db.query(u, v)[0])
        self.assertFalse(db.source_lemma_checks())

    def test_source_depth_base_case_needs_explicit_convention(self):
        db = PowerAnchorIndex(2)
        db.append(())
        self.assertEqual(db.labels[0].rank, 1)
        self.assertEqual(db.labels[0].power, 0)
        self.assertEqual(db.anchor_depth(0), 1)
        # Source Lemma 9 prints B*floor(log_B(rank))=0 while
        # anchor depth was defined as length([v])=1, so do not assert it.
        self.assertEqual(db.report()["source_depth_convention"],
                         "UNRESOLVED_LENGTH_VS_ZERO_BASE_CASE")

    def test_multi_parent_and_felsner_invariants(self):
        trace = ((), (), (0,), (1,), (2, 3), (0, 1, 4),
                 (2, 4, 5), (0, 6))
        for b in (2, 3, 5):
            db = PowerAnchorIndex(b)
            for p in trace:
                db.append(p)
            self.assertFalse(db.partition.invariant_errors())
            self.assertFalse(db.source_lemma_checks())
            for u in range(len(trace)):
                for v in range(len(trace)):
                    self.assertEqual(db.query(u, v)[0],
                                     source_dfs(trace, u, v))

    def test_input_validation_and_rank_increasing(self):
        with self.assertRaises(ValueError):
            PowerAnchorIndex(1)
        db = PowerAnchorIndex(2)
        with self.assertRaises(ValueError):
            db.append((0,))
        db.append(())
        with self.assertRaises(ValueError):
            db.append((0, 0))
        db.append((0,))
        self.assertGreater(db.labels[1].rank, db.labels[0].rank)
        with self.assertRaises(ValueError):
            db.query(-1, 0)


if __name__ == "__main__":
    unittest.main()
