"""TOM-001-C: minimal deterministic counterexamples, NOT novelty/proof claims.

These unit tests falsify overbroad contracts in TOM-001-B.
They are intentionally isolated from LENT-001 research/run_all.py.
"""

from itertools import product
import unittest


def truth_table_output(table: int, x: int, y: int) -> int:
    """Read the (x,y) bit in the 16 possible binary Boolean functions."""
    if not (0 <= table < 16 and x in (0, 1) and y in (0, 1)):
        raise ValueError("expected a 2-input Boolean function")
    return (table >> (2 * x + y)) & 1


def positional_pairs(items):
    """Deliberately naive, stable-by-position rather than stable-by-content."""
    return tuple(tuple(items[i:i + 2]) for i in range(0, len(items), 2))


class TomCounterexampleTests(unittest.TestCase):
    def test_O01_old_result_does_not_decide_no_effect(self):
        # OR truth table: 00->0, 01->1, 10->1, 11->1.
        OR = 0b1110
        old_a, old_b = (1, 0), (1, 1)
        self.assertEqual(truth_table_output(OR, *old_a), 1)
        self.assertEqual(truth_table_output(OR, *old_b), 1)
        # Identical request: set first input to 0.
        new_a = (0, old_a[1])
        new_b = (0, old_b[1])
        self.assertEqual(truth_table_output(OR, *new_a), 0)
        self.assertEqual(truth_table_output(OR, *new_b), 1)

    def test_O02_individual_no_effect_does_not_imply_joint_no_effect(self):
        # AND truth table: only 11->1.
        AND = 0b1000
        base = truth_table_output(AND, 0, 0)
        self.assertEqual(base, 0)
        self.assertEqual(truth_table_output(AND, 1, 0), base)
        self.assertEqual(truth_table_output(AND, 0, 1), base)
        self.assertNotEqual(truth_table_output(AND, 1, 1), base)

    def test_O02_counterexample_is_found_by_exhausting_all_boolean_tables(self):
        offenders = []
        for table in range(16):
            before = truth_table_output(table, 0, 0)
            if (truth_table_output(table, 1, 0) == before
                    and truth_table_output(table, 0, 1) == before
                    and truth_table_output(table, 1, 1) != before):
                offenders.append(table)
        self.assertIn(0b1000, offenders)
        self.assertGreater(len(offenders), 0)

    def test_O06_prepend_destabilizes_all_positional_pairs(self):
        for n in (2, 4, 8, 32, 64):
            before = positional_pairs(list(range(n)))
            after = positional_pairs([-1] + list(range(n)))
            self.assertTrue(set(before).isdisjoint(set(after)))
            self.assertEqual(len(before), n // 2)

    def test_truth_tables_exhaust_all_four_input_assignments(self):
        # Checks that oracle covers exactly 16 distinct binary functions.
        fingerprints = set()
        for table in range(16):
            fingerprints.add(tuple(
                truth_table_output(table, x, y)
                for x, y in product((0, 1), repeat=2)
            ))
        self.assertEqual(len(fingerprints), 16)


if __name__ == "__main__":
    unittest.main()
