"""UCT-004 G2 finite countermodel: nonlinear local tests can cover larger
honest parity fibers than affine-rank arguments permit. This DOES NOT prove
that the general b>=ceil(n/p)-1 inequality is false.
"""
from fractions import Fraction
import unittest


def weight(x):
    return x.bit_count()


def parity(x):
    return weight(x) & 1


def triple_weight(x, omission):
    return weight(x & ~(1 << omission))


def accept_chance(x, claim, proof):
    """Explicit fully sound n=4,p<=3,b=1 protocol, hidden private coins."""
    if claim == 0:
        # Four private equally likely seeds: omit one position, read 3 bits.
        if proof == 0:
            # Weight-two witnesses form a NONLINEAR six-element class.
            return Fraction(sum(triple_weight(x, i) in (1, 2)
                                for i in range(4)), 4)
        # Remaining even states have weight zero or four.
        return Fraction(sum(triple_weight(x, i) in (0, 3)
                            for i in range(4)), 4)

    # For the odd-parity claim, use the fully linear block-protocol
    # with blocks [0,1,2], [3], and one prover bit.
    x_first = parity(x & 0b0111)
    x_last = (x >> 3) & 1
    alleged_first = proof
    alleged_last = claim ^ proof
    return Fraction((x_first == alleged_first)
                    + (x_last == alleged_last), 2)


def certifiable_same_parity_class(n, cap, honest_set, claim=0):
    """Each false input can be separated from honest set by some cap-bit
    projection; equivalently, there exist private-coin local tests with
    one-sided completeness for the class and soundness strictly below 1.
    """
    false_inputs = [x for x in range(1 << n) if parity(x) != claim]
    for y in false_inputs:
        possible = False
        for support in range(1, 1 << n):
            if support.bit_count() > cap:
                continue
            if all((x & support) != (y & support) for x in honest_set):
                possible = True
                break
        if not possible:
            return False
    return True


class Uct004NonlinearScopeTests(unittest.TestCase):
    def test_six_honest_weight_two_states_exceed_linear_affine_fiber_cap(self):
        n, p = 4, 3
        weight_two = tuple(x for x in range(1 << n) if weight(x) == 2)
        self.assertEqual(weight_two, (3, 5, 6, 9, 10, 12))
        self.assertEqual(len(weight_two), 6)
        # Affine linear rank bound would cap a single proof fiber at 4.
        self.assertGreater(len(weight_two), 1 << (n - 2))
        self.assertTrue(certifiable_same_parity_class(n, p, weight_two))

    def test_full_protocol_perfect_completeness_every_state(self):
        for x in range(16):
            claim = parity(x)
            if claim == 0:
                proof = 0 if weight(x) == 2 else 1
            else:
                proof = parity(x & 0b0111)
            self.assertEqual(accept_chance(x, claim, proof), 1)

    def test_all_false_claims_and_both_proofs_have_soundness_below_one(self):
        worst = Fraction(0)
        for x in range(16):
            wrong = parity(x) ^ 1
            for proof in (0, 1):
                chance = accept_chance(x, wrong, proof)
                self.assertLessEqual(chance, Fraction(3, 4))
                worst = max(worst, chance)
        self.assertEqual(worst, Fraction(3, 4))

    def test_full_small_nonlinear_fiber_enumeration(self):
        for n in range(2, 5):
            even = [x for x in range(1 << n) if parity(x) == 0]
            for p in range(1, n):
                best = 0
                for pattern in range(1, 1 << len(even)):
                    subset = tuple(even[i] for i in range(len(even))
                                   if pattern & (1 << i))
                    if len(subset) <= best:
                        continue
                    if certifiable_same_parity_class(n, p, subset):
                        best = len(subset)
                if (n, p) == (4, 3):
                    self.assertEqual(best, 6)
                if p == 1:
                    self.assertEqual(best, 1)


if __name__ == "__main__":
    unittest.main()
