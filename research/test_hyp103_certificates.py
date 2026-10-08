"""HYP-103 G0: independent exact old-root batch certificate oracles.

Finite enumeration confirms a self-contained elementary certificate-complexity
reduction. It does not prove complexity bounds for arbitrary n/treewidth,
optimal verifier runtime, or a novel research theorem.
"""
import itertools
import unittest


def eval_f(table_bits, input_bits):
    """The truth-table entry for the input, indexed by input bit mask."""
    return (table_bits >> input_bits) & 1


def overwrite(input_bits, update_codes, n):
    """Apply simultaneous assignments: 0=keep, 1=write-0, 2=write-1."""
    value = input_bits
    for pos in range(n):
        code = update_codes[pos]
        if code == 1:
            value &= ~(1 << pos)
        elif code == 2:
            value |= (1 << pos)
    return value


def brute_consistency_certificates(table_bits, n, x, update_codes):
    """Method A: every completion of the old-root promise must agree."""
    old_root = eval_f(table_bits, x)
    target = eval_f(table_bits, overwrite(x, update_codes, n))
    feasible = tuple(y for y in range(1 << n)
                     if eval_f(table_bits, y) == old_root)
    valid = set()
    for probes in range(1 << n):
        if all(eval_f(table_bits, overwrite(y, update_codes, n)) == target
               for y in feasible if (y & probes) == (x & probes)):
            valid.add(probes)
    return valid


def independently_hitting_certificates(table_bits, n, x, update_codes):
    """Method B: distinguish every opposite-label alternative old input."""
    original_label = eval_f(table_bits, x)
    def updated_label(input_bits):
        bits = list((input_bits >> i) & 1 for i in range(n))
        for i, code in enumerate(update_codes):
            if code:
                bits[i] = code - 1
        index = sum(bit << i for i, bit in enumerate(bits))
        return (table_bits >> index) & 1

    actual = updated_label(x)
    alternate_differences = []
    for other in itertools.product((0, 1), repeat=n):
        y = sum(bit << i for i, bit in enumerate(other))
        if ((table_bits >> y) & 1) == original_label and updated_label(y) != actual:
            alternate_differences.append(x ^ y)
    return {mask for mask in range(1 << n)
            if all(mask & difference for difference in alternate_differences)}


class Hyp103OldRootCertificateTests(unittest.TestCase):
    def test_all_boolean_functions_all_inputs_all_overwrite_batches_n_le_3(self):
        instances = 0
        for n in range(4):
            for f in range(1 << (1 << n)):
                for update in itertools.product((0, 1, 2), repeat=n):
                    for x in range(1 << n):
                        direct = brute_consistency_certificates(f, n, x, update)
                        hitting = independently_hitting_certificates(f, n, x, update)
                        self.assertEqual(direct, hitting,
                                         (n, f, x, update))
                        self.assertTrue(direct)  # full old state always suffices
                        instances += 1
        self.assertEqual(instances, 2 + 4*2*3 + 16*4*9 + 256*8*27)

    def test_two_singletons_need_probes_but_joint_overwrite_needs_none(self):
        # For input x=(a,b) and truth table f(a,b)=a AND b,
        # entry index 3 is true -> table 0b1000 = 8.
        table, n, old = 8, 2, 0
        single_a = brute_consistency_certificates(table, n, old, (2, 0))
        single_b = brute_consistency_certificates(table, n, old, (0, 2))
        joint = brute_consistency_certificates(table, n, old, (2, 2))
        self.assertEqual(min(mask.bit_count() for mask in single_a), 1)
        self.assertEqual(min(mask.bit_count() for mask in single_b), 1)
        self.assertEqual(min(mask.bit_count() for mask in joint), 0)
        self.assertEqual(eval_f(table, old), 0)
        self.assertEqual(eval_f(table, overwrite(old, (2, 2), n)), 1)

    def test_noop_requires_no_probes_and_empty_function_domain(self):
        for n in range(4):
            for f in range(1 << (1 << n)):
                for x in range(1 << n):
                    self.assertIn(0, brute_consistency_certificates(
                        f, n, x, (0,) * n))

    def test_trusted_full_state_must_not_be_free(self):
        # For AND, old-root 0 does NOT tell which other old bit is zero.
        # Setting a:=1, from x=00 needs reading b; accepting no probes
        # would be unsound on old input (0,1), which shares old root 0.
        self.assertNotIn(0, brute_consistency_certificates(8, 2, 0, (2, 0)))
        self.assertEqual(eval_f(8, 0), eval_f(8, 2))
        self.assertNotEqual(
            eval_f(8, overwrite(0, (2, 0), 2)),
            eval_f(8, overwrite(2, (2, 0), 2)))


if __name__ == "__main__":
    unittest.main()
