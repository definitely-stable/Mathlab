"""Independent DAG-002 G2-B2-A tests, no paper novelty assertion."""
import unittest
from dag002_g2b2_felsner import (
    FelsnerUpGrowing, exact_width, five_vertex_census, source_dfs
)


class FelsnerTests(unittest.TestCase):
    def test_all_1024_five_vertex_graphs_prefix_invariants(self):
        summary = five_vertex_census()
        self.assertEqual(summary["graphs"], 1024)
        self.assertEqual(summary["prefixes"], 5120)

    def test_family_exchange_realizes_theorem_35(self):
        db = FelsnerUpGrowing()
        events = [db.append(p) for p in (
            (), (), (0,), (1,), (2, 3), (0, 1, 2, 3, 4)
        )]
        self.assertEqual(events[0].level, 1)
        self.assertEqual(events[1].level, 2)
        self.assertFalse(events[2].created)
        self.assertGreaterEqual(events[3].level, 1)
        self.assertFalse(db.invariant_errors())

    def test_ancestor_oracle_agrees_with_independent_dfs(self):
        parents = ((), (), (0,), (1,), (2, 3), (4,), (3, 5))
        db = FelsnerUpGrowing()
        for p in parents:
            db.append(p)
        for u in range(7):
            for v in range(7):
                self.assertEqual(db.reaches(u, v), source_dfs(parents, u, v))
        self.assertFalse(db.invariant_errors())

    def test_adversarial_and_wide_traces(self):
        traces = [
            [()] * 100,
            [()] + [(v - 1,) for v in range(1, 100)],
            [()] * 12 + [tuple(range(12))]
              + [(v - 1,) for v in range(13, 100)],
            [tuple(i for i in range(v) if (i * 43 + v * 17) % 11 < 3)
             for v in range(100)],
        ]
        for trace in traces:
            db = FelsnerUpGrowing()
            for v, p in enumerate(trace):
                db.append(p)
                self.assertFalse(db.invariant_errors(), (v, db.report()))
                self.assertEqual(db.assignment[v], db.steps[v].chain)
            self.assertEqual(len(db.chains), sum(len(f) for f in db.families))
        self.assertEqual(len(FelsnerUpGrowing().families), 0)

    def test_zero_and_old_old_stability(self):
        db = FelsnerUpGrowing()
        for p in ((), (0,), (0,), (1, 2)):
            db.append(p)
        old = tuple(db.assignment)
        past = [[db.reaches(u, v) for v in range(4)] for u in range(4)]
        db.append((3,))
        self.assertEqual(tuple(db.assignment[:4]), old)
        self.assertEqual(past,
                         [[db.reaches(u, v) for v in range(4)]
                          for u in range(4)])

    def test_reject_invalid_commands_and_exact_width_small(self):
        db = FelsnerUpGrowing()
        for bad in ((0,), (2,), (-1,), (1, 0), (0, 0)):
            with self.assertRaises(ValueError):
                db.append(bad)
        db.append(())
        with self.assertRaises(ValueError):
            db.append((1,))
        db.append(())
        self.assertEqual(exact_width(db.anc), 2)
        db.append((0, 1))
        self.assertEqual(exact_width(db.anc), 2)
        with self.assertRaises(ValueError):
            db.reaches(-1, 0)
        with self.assertRaises(ValueError):
            exact_width([1] * 10)

    def test_no_hidden_priced_oracle_claim(self):
        db = FelsnerUpGrowing()
        for p in ((), (), (0, 1)):
            db.append(p)
        report = db.report()
        self.assertEqual(report["unpriced_ancestor_oracle_bits"], 9)
        self.assertEqual(report["parent_input_bits"], 3)
        self.assertIn("CLASSICAL", report["proof_status"])
        self.assertFalse(report["invariant_errors"])


if __name__ == "__main__":
    unittest.main()
