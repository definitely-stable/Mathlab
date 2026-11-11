"""Independent finite-model falsifiers and deliberately restricted brute oracle."""
import itertools
import unittest

from dag002_g1c2_synthesis import (
    ToyModel, Budget, action_alphabet, synthesize_invariant,
    verify_certificate, tree_cost, examples,
)


def independent_one_read_exists(m, budget, initial):
    """Independent literal enumeration; no synthesized tree or transition helpers."""
    assert m.H == 0 and m.N <= 2 and m.n == 1 and budget.query_reads >= m.N
    actions = (None,) + tuple((addr, value) for addr in range(m.N)
                              for value in (0, 1))
    programs = tuple((None, a, a) for a in actions)
    if budget.update_reads:
        programs += tuple((addr, a, c) for addr in range(m.N)
                          for a in actions for c in actions)

    def updated(word, program):
        address, left, right = program
        action = right if address is not None and ((word >> address) & 1) else left
        if action is None:
            return word
        idx, value = action
        return (word & ~(1 << idx)) | (value << idx)

    domain = 1 << m.N
    for subset_mask in range(1, 1 << domain):
        if not (subset_mask & (1 << initial)):
            continue
        group = tuple(s for s in range(domain) if subset_mask & (1 << s))
        valid = True
        for delta in m.deltas:
            def uniform(p):
                for state in group:
                    addr, left, right = p
                    choice = right if addr is not None and (state >> addr) & 1 else left
                    if choice is not None and budget.remote_writes == 0:
                        return False
                    dest = updated(state, p)
                    if dest not in group or m.decoder[dest] != (m.decoder[state] ^ delta):
                        return False
                return True
            if not any(uniform(program) for program in programs):
                valid = False
                break
        if valid:
            return True
    return False


class G1C2ExactTests(unittest.TestCase):
    def test_full_read_relaxation_does_not_imply_zero_update_reads(self):
        direct, _ = examples()
        self.assertIsNone(synthesize_invariant(direct, Budget(1, 0, 1, 0), 0))
        solution = synthesize_invariant(direct, Budget(1, 1, 1, 0), 0)
        self.assertEqual(solution[0], frozenset((0, 1)))
        self.assertTrue(verify_certificate(direct, Budget(1, 1, 1, 0), solution, 0))
        self.assertIsNone(synthesize_invariant(direct, Budget(0, 1, 1, 0), 0))
        self.assertIsNone(synthesize_invariant(direct, Budget(1, 1, 1, 0,
                                                              net_changes=0), 0))

    def test_h1_is_a_paid_escape_not_unpriced_remote_information(self):
        _, trusted = examples()
        b = Budget(0, 0, 0, 1, net_changes=0)
        sol = synthesize_invariant(trusted, b, 0)
        self.assertEqual(sol[0], frozenset((0, 1)))
        self.assertTrue(verify_certificate(trusted, b, sol, 0))
        self.assertIsNone(synthesize_invariant(trusted, Budget(0, 0, 0, 0), 0))
        self.assertIsNone(synthesize_invariant(trusted, Budget(0, 0, 0, 1, 0), 0))
        self.assertFalse(verify_certificate(trusted,
            Budget(0, 0, 0, 1, sol[2] - 1), sol, 0))

    def test_independent_bruteforce_all_binary_decoders_n_le_two_cells(self):
        for N in range(3):
            for decoder in itertools.product((0, 1), repeat=1 << N):
                model = ToyModel(1, N, 0, decoder, (0, 1))
                for R in (0, 1):
                    budget = Budget(N, R, 1, 0)
                    found = synthesize_invariant(model, budget, 0)
                    self.assertEqual(found is not None,
                        independent_one_read_exists(model, budget, 0),
                        (N, decoder, R))
                    if found:
                        self.assertTrue(verify_certificate(model, budget, found, 0))

    def test_restricted_invariant_must_not_be_silently_full_domain(self):
        # XOR of 2 remote bits needs P=2 on ALL four words, but a
        # dynamically maintained 2-word subcode admits P=1.
        model = ToyModel(1, 2, 0, (0, 1, 1, 0), (0, 1))
        self.assertIsNotNone(synthesize_invariant(model, Budget(1, 1, 1, 0), 0))
        full = tuple(range(4))
        self.assertIsNone(synthesize_invariant(model, Budget(1, 1, 1, 0),
                                               0, full))
        cert = synthesize_invariant(model, Budget(2, 1, 1, 0), 0, full)
        self.assertIsNotNone(cert)
        self.assertEqual(cert[0], frozenset(full))
        self.assertTrue(verify_certificate(model, Budget(2, 1, 1, 0), cert, 0))

    def test_exact_program_bits_only_for_stated_prefix_grammar(self):
        direct, _ = examples()
        b = Budget(1, 1, 1, 0)
        cert = synthesize_invariant(direct, b, 0)
        actual = sum(tree_cost(t, direct.N, (2 if key[0] == "query"
                    else len(action_alphabet(direct))))
                     for key, t in cert[1].items())
        self.assertEqual(actual, cert[2])
        self.assertIsNone(synthesize_invariant(direct,
            Budget(1, 1, 1, 0, cert[2] - 1), 0))

    def test_input_validation_and_certificate_tampering(self):
        direct, _ = examples()
        bad = [
            dict(n=True, N=1, H=0, decoder=(0, 1), deltas=(0, 1)),
            dict(n=1, N=2, H=2, decoder=(0,) * 16, deltas=(0, 1)),
            dict(n=1, N=1, H=0, decoder=(0, 2), deltas=(0, 1)),
            dict(n=1, N=1, H=0, decoder=(0, 1), deltas=(1, 1))]
        for kwargs in bad:
            with self.assertRaises(ValueError):
                ToyModel(**kwargs)
        with self.assertRaises(ValueError):
            Budget(-1, 0, 0, 0)
        with self.assertRaises(ValueError):
            Budget(0, 3, 1, 0)
        with self.assertRaises(ValueError):
            Budget(1, 1, 1, 0, net_changes=2)
        with self.assertRaises(ValueError):
            synthesize_invariant(direct, Budget(1, 1, 1, 1), 0)
        with self.assertRaises(ValueError):
            synthesize_invariant(direct, Budget(1, 1, 1, 0), 3)
        with self.assertRaises(ValueError):
            synthesize_invariant(direct, Budget(1, 1, 1, 0), 0, (1, 1))
        live, tree, bits = synthesize_invariant(direct, Budget(1, 1, 1, 0), 0)
        self.assertFalse(verify_certificate(direct, Budget(1, 1, 1, 0),
                                            (live, tree, bits + 1), 0))


if __name__ == "__main__":
    unittest.main()
